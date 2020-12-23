class Car:
    def drive_forward(self):
        print("전진하기")

    def drive_back(self):
        print("후진하기")

    def rotate_right(self):
        print("우회전하기")

    def rotate_left(self):
        print("좌회전하기")

    def stop(self):
        print("정지하기")
        print("----------------")

car1=Car()
car2=Car()
car3=Car()

print("[car1 작동순서]")
car1.drive_forward()
car1.rotate_right()
car1.drive_forward()
car1.rotate_right()
car1.stop()

print("[car2 작동순서]")
car2.drive_back()
car2.stop()

print("[car3 작동순서]")
car3.rotate_right()
car3.drive_forward()
car3.stop()
