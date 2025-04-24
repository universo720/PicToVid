
import os
import cv2
from glob import glob

def convert_images_to_video(output_filename="output.mp4", fps=2, ext="png"):
    # Buscar imágenes en el directorio actual con la extensión especificada
    image_files = sorted(glob(f"*.{ext}"))
    if not image_files:
        print(f"❌ No se encontraron imágenes .{ext} en esta carpeta.")
        return

    # Leer primera imagen para obtener dimensiones
    first_img = cv2.imread(image_files[0])
    if first_img is None:
        print(f"❌ Error al leer la imagen {image_files[0]}")
        return
    height, width, _ = first_img.shape

    # Crear objeto para escribir video
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))

    # Añadir imágenes al video
    for img_file in image_files:
        img = cv2.imread(img_file)
        if img.shape[:2] != (height, width):
            img = cv2.resize(img, (width, height))
        video.write(img)

    video.release()
    print(f"✅ Video generado exitosamente: {output_filename}")

if __name__ == "__main__":
    print("🎞️  Generador de video desde imágenes")
    ext = input("Extensión de las imágenes (ej: png, jpg, jpeg): ").strip() or "png"
    fps = input("Frames por segundo (FPS) [por defecto 2]: ").strip()
    fps = int(fps) if fps.isdigit() else 2
    output = input("Nombre del archivo de salida (ej: video.mp4) [por defecto output.mp4]: ").strip() or "output.mp4"

    convert_images_to_video(output_filename=output, fps=fps, ext=ext)
