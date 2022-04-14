from PIL import Image

image_1 = Image.open(r'D:\College\Semester 4\CE259 - Python Programming\Final subs\Practical 10\SEM_3_result.JPG')
im_1 = image_1.convert('RGB')
im_1.save(r'D:\College\Semester 4\CE259 - Python Programming\Final subs\Practical 10\my_result.pdf', save_all=True)
print("PDF created", end = " ")