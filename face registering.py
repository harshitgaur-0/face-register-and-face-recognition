
image_encoding = []
names = []
while True:
    demand = input("SIGNUP OR SIGNIN").upper()
    if demand == "SIGNUP":
        import cv2
        import time
        import face_recognition
        video_capture = cv2.VideoCapture(0)
        result = True
        name = input("enter your name")
        image_ = 0
        while result:
            print("LOOK IN THE CAMERA for 6 second")
            time.sleep(5)
            cap, frame = video_capture.read()
            cv2.imwrite("{}.jpg".format(name), frame)
            image_ = "{}.jpg".format(name)
            result = False
        video_capture.release()
        cv2.destroyAllWindows()
        image = face_recognition.load_image_file(image_)
        image_encoding.append((face_recognition.face_encodings(image))[0])
        names.append(name)
    elif demand == "SIGNIN":
        import cv2
        import time
        import face_recognition
        unknown_video_captured = cv2.VideoCapture(0)
        result = True
        while result:
            print("Look in the camera for 6 seconds")
            time.sleep(5)
            cap, frame = unknown_video_captured.read()
            cv2.imwrite("unknown.jpg", frame)
            result = False
        unknown_video_captured.release()
        cv2.destroyAllWindows()
        image_unknown = face_recognition.load_image_file("unknown.jpg")
        unknown_face_encodings = face_recognition.face_encodings(image_unknown)
        for unknown_face_encoding in unknown_face_encodings:
            re = face_recognition.compare_faces(image_encoding, unknown_face_encoding, tolerance=0.6)
            name = "Your face is not registered"
            for i in range(len(image_encoding)):
                if re[i]:
                    name = (names[i])
                    break
                else:
                    continue
            print(name)
    else:
        print("WRONG COMMAND IS GIVEN")



