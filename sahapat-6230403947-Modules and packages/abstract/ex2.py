from abc import ABC, abstractmethod


class Image(ABC):
    @abstractmethod
    def load_image(self, file):
        print(f"loading bitmap file {file}")

    @abstractmethod
    def save_image(self, file):
        print(f"saving bitmap file {file}")


class Bitmap(Image):
    def load_image(self, file):
        super(Bitmap, self).load_image(file)

    def save_image(self, file):
        super(Bitmap, self).save_image(file)


class Jpeg(Image):
    def load_image(self, file):
        super(Jpeg, self).load_image(file)

    def save_image(self, file):
        super(Jpeg, self).save_image(file)


if __name__ == '__main__':
    bitmap1 = Bitmap()
    bitmap1.save_image("kku.bmp")
    bitmap1.load_image("kku.bmp")
    jpeg1 = Jpeg()
    jpeg1.save_image("en.jpg")
    jpeg1.load_image("en.jpg")
