# pip install easyocr or pip install -r requirements.txt
import easyocr


def text_recognition(file_path):
    reader = easyocr.Reader(["ru", "en", "es", "it", "zh", "de", "fr"])
    result = reader.readtext(file_path, detail=0, paragraph=True)

    with open('result.txt', "w") as file:
        for line in result:
            file.write(f"{line}\n\n")

    return f"Result wrote into result.txt"


def main():
    file_path = '/Users/Wolfram_3387/PycharmProjects/Kenny/img.png'
    print(text_recognition(file_path=file_path))


if __name__ == "__main__":
    main()
