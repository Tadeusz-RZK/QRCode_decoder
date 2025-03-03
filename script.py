import cv2
import numpy as np
from pyzbar.pyzbar import decode
import argparse


def decode_qr_code(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Erreur: Impossible de charger l'image {image_path}")
        return []

    decoded_objects = decode(image)
    if not decoded_objects:
        print("Aucun QR code détecté dans l'image.")
        return []

    results = []
    for obj in decoded_objects:
        try:
            data = obj.data.decode('utf-8')
        except UnicodeDecodeError:
            data = obj.data

        print(f"Type: {obj.type}")
        print(f"Données: {data}")
        print("-" * 30)

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('image', help='Path to the input QRCode')
    args = parser.parse_args()

    decode_qr_code(args.image)
