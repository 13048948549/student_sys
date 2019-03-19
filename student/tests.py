from django.test import TestCase, Client

# Create your tests here.
from student.models import Student




class StudentTestCase(TestCase):

    def setUp(self):
        Student.objects.create(
            name = 'zhengziyu',
            sex = 1,
            email = '826373691@qq.com',
            profession = 'soft',
            qq = '3333zz',
            phone = '2222'
        )

    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name = 'huyang',
            sex = 1,
            email = '826375159qq.com',
            profession = 'soft',
            qq = '2222zz',
            phone = '111'
        )
        self.assertEqual(student.sex_show,'男','性别字段内容跟展示字段不一致')

    def test_filter(self):
        Student.objects.create(
            name = 'huyang',
            sex = 1,
            email = '826373691qq.com',
            qq = '2131',
            phone = '1212'
        )
        name = 'huyang'
        students = Student.objects.filter(name = name)
        self.assertEqual(students.count(),1,'应该只存在一个名称为{}的记录'.format(name))

    def test_get_index(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code,200,'status code must be 200!')

    def test_post_student(self):
        client = Client()
        data = dict(
            name = 'test_for_post',
            sex = 1,
            email = '123423@qq.com',
            profession = 'soft',
            qq = '2222',
            phone = '3222'
        )
       # response = client.post('/',data)
       # self.assertTrue(response.status_code,302,'status code must be 302!')

        response = client.get('/',data)
        self.assertTrue(b'test_for_post' in response.content,'response content must contain ‘test_for_post’')