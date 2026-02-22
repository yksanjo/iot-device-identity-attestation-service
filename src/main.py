from datetime import datetime, timezone


def main() -> None:
    print("iot-device-identity-attestation-service initialized at", datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    main()
