from setuptools import setup, find_packages

setup(
    name="alice",  # Replace with your desired package name
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    install_requires=[
        "numpy",
        "connexion[flask,uvicorn,swagger-ui]",
        "spidev",
        "smbus",
        "pillow",
        "gpiozero",
        "lgpio",
        "flask_socketio",
    ],
    extras_require={
        "dev": ["pytest", "flake8"],
    },
    description="Secure sum on raspberry pi",
    author="christiangoelz",
    author_email="c.goelz@gmx.de",
    python_requires=">=3.11",
)