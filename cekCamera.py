import cv2

def get_camera_list():
    camera_list = []
    for i in range(10):  # Coba untuk indeks kamera dari 0 hingga 9
        cap = cv2.VideoCapture(i)
        if not cap.read()[0]:
            break
        camera_list.append(i)
        cap.release()

    return camera_list

if __name__ == "__main__":
    cameras = get_camera_list()

    if cameras:
        print("Daftar kamera yang tersedia:")
        for idx, camera in enumerate(cameras):
            print(f"Kamera {idx + 1}: Camera Index {camera}")
    else:
        print("Tidak ada kamera yang ditemukan.")
