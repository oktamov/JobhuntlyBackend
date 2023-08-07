from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True, min_length=6)

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "password",
        )
        read_only_fields = ("id",)

    def validate(self, attrs):
        email = attrs.get("email")
        user = User.objects.filter(email=email).exists() if email else None
        if user:
            raise ValidationError('Email is already taken.')
        return super().validate(attrs)

    def create(self, validated_data):
        password1 = validated_data.pop("password1", None)
        user = User(**validated_data)
        user.set_password(password1)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True, style={"input_type": "password"})

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        user = User.objects.filter(username=username).first()

        if user:
            if not user.is_active:
                raise serializers.ValidationError("User account is disabled.")
            if not user.check_password(password):
                raise serializers.ValidationError("Invalid password.")
        else:
            raise serializers.ValidationError("User not found.")

        refresh = RefreshToken.for_user(user)
        attrs["tokens"] = {"access": str(refresh.access_token), "refresh": str(refresh)}

        attrs["user"] = user
        return attrs
