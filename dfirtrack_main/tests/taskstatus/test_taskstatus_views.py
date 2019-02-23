from django.contrib.auth.models import User
from django.test import TestCase
from dfirtrack_main.models import Taskstatus
from dfirtrack_main.views import taskstatuss_views
import urllib.parse

class TaskstatusViewTestCase(TestCase):
    """ taskstatus view tests """

    @classmethod
    def setUpTestData(cls):

        # create object
        Taskstatus.objects.create(taskstatus_name='taskstatus_1')
        # create user
        test_user = User.objects.create_user(username='testuser_taskstatus', password='TZjmjiUQviOnIEral6l9')
        test_user.save()

    def test_taskstatuss_list_not_logged_in(self):

        # create url
        destination = '/login/?next=' + urllib.parse.quote('/taskstatuss/', safe='')
        # get response
        response = self.client.get('/taskstatuss/', follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_taskstatuss_list_logged_in(self):

        # login testuser
        login = self.client.login(username='testuser_taskstatus', password='TZjmjiUQviOnIEral6l9')
        # get response
        response = self.client.get('/taskstatuss/')
        # compare
        self.assertEqual(response.status_code, 200)

    def test_taskstatuss_list_template(self):

        # login testuser
        login = self.client.login(username='testuser_taskstatus', password='TZjmjiUQviOnIEral6l9')
        # get response
        response = self.client.get('/taskstatuss/')
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/taskstatus/taskstatuss_list.html')

    def test_taskstatuss_list_get_user_context(self):

        # login testuser
        login = self.client.login(username='testuser_taskstatus', password='TZjmjiUQviOnIEral6l9')
        # get response
        response = self.client.get('/taskstatuss/')
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_taskstatus')

    def test_taskstatuss_detail_not_logged_in(self):

        # get object
        taskstatus_1 = Taskstatus.objects.get(taskstatus_name='taskstatus_1')
        # create url
        destination = '/login/?next=' + urllib.parse.quote('/taskstatuss/' + str(taskstatus_1.taskstatus_id), safe='')
        # get response
        response = self.client.get('/taskstatuss/' + str(taskstatus_1.taskstatus_id), follow=True)
        # compare
        self.assertRedirects(response, destination, status_code=302, target_status_code=200)

    def test_taskstatuss_detail_logged_in(self):

        # get object
        taskstatus_1 = Taskstatus.objects.get(taskstatus_name='taskstatus_1')
        # login testuser
        login = self.client.login(username='testuser_taskstatus', password='TZjmjiUQviOnIEral6l9')
        # get response
        response = self.client.get('/taskstatuss/' + str(taskstatus_1.taskstatus_id))
        # compare
        self.assertEqual(response.status_code, 200)

    def test_taskstatuss_detail_template(self):

        # get object
        taskstatus_1 = Taskstatus.objects.get(taskstatus_name='taskstatus_1')
        # login testuser
        login = self.client.login(username='testuser_taskstatus', password='TZjmjiUQviOnIEral6l9')
        # get response
        response = self.client.get('/taskstatuss/' + str(taskstatus_1.taskstatus_id))
        # compare
        self.assertTemplateUsed(response, 'dfirtrack_main/taskstatus/taskstatuss_detail.html')

    def test_taskstatuss_detail_get_user_context(self):

        # get object
        taskstatus_1 = Taskstatus.objects.get(taskstatus_name='taskstatus_1')
        # login testuser
        login = self.client.login(username='testuser_taskstatus', password='TZjmjiUQviOnIEral6l9')
        # get response
        response = self.client.get('/taskstatuss/' + str(taskstatus_1.taskstatus_id))
        # compare
        self.assertEqual(str(response.context['user']), 'testuser_taskstatus')

#    def test_taskstatuss_detail_logged_in_not_existing(self):
#
#        # login testuser
#        login = self.client.login(username='testuser_taskstatus', password='TZjmjiUQviOnIEral6l9')
#        # get response
#        response = self.client.get('/taskstatuss/x')
#        # compare
#        self.assertEqual(response.status_code, 404)