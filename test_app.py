from app import app
from unittest import TestCase


class Tests(TestCase):
    def test_root(self):
        with app.test_client() as client:
            res = client.get('/homepage')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Welcome to Blogly!</h1>', html)

    def test_homepage(self):
        with app.test_client() as client:
            res = client.get('/homepage')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Welcome to Blogly!</h1>', html)

    def test_form(self):
        with app.test_client() as client:
            res = client.get('/add-user')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h2>Add New User</h2>', html)

    def test_add_user(self):
        with app.test_client() as client:
            res = client.post('/add-user', data={'first_name': 'John', 'last_name': 'Smith',
                              'image_url': 'https://img.freepik.com/free-photo/handsome-confident-smiling-man-with-hands-crossed-chest_176420-18743.jpg?w=2000'})
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h3>John Smith</h3>', html)

    # def test_user(self):
    #     with app.test_client() as client:
    #         res = client.get('/1')
    #         html = res.get_data(as_test=True)

    #         self.assertEqual(res.status_code, 200)
    #         self.assertIn('<button class="edit">Edit User</button>', html)

    def test_posts(self):
        with app.test_client() as client:
            res = client.get('/posts')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h3>Posts</h3>', html)

    def test_all_users(self):
        with app.test_client() as client:
            res = client.get('/all-users')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h3>Users</h3>', html)

    def test_new_post(self):
        with app.test_client() as client:
            res = client.post('/new-post', data={'user': '1'})
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h2>Make Post</h2>', html)

    def test_add_post(self):
        with app.test_client() as client:
            res = client.post(
                '/add-post', data={'user-id': '1', 'title': 'test', 'content': 'testing'})
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<p>test</p>', html)

    def test_edit_post_html(self):
        with app.test_client() as client:
            res = client.post('edit-post_html', data={'post-id': '1'})
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<form action="/edit-post" method="post">', html)

    def test_delete_post(self):
        with app.test_client() as client:
            res = client.post('/delete-post', data={'post-id': '1'})
           

            self.assertEqual(res.status_code, 200)

    def test_edit_user_html(self):
        with app.test_client() as client:
            res = client.post('/edit-user', data={'user-id': '1'})
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h2>Edit User</h2>', html)

    # def test_edit_user(self):
    #     with app.test_client() as client:
    #         res = client.post('/editted-user', data={'id': '1', 'first_name': 'Stacey', 'last_name': 'Allen',
    #                           'image_url': 'https://images.pexels.com/photos/733872/pexels-photo-733872.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500'})
    #         html = res.get_data(as_text=True)

    #         self.assertEqual(res.status_code, 200)
    #         self.assertIn('<h3>Stacey Allen</h3>', html)
            
    def test_delete_user(self):
        with app.test_client() as client:
            res = client.post('/delete-user', data={'user':'1'})

            self.assertEqual(res.status_code, 200)

    def test_tag_html(self):
        with app.test_client() as client:
            res = client.get('/tag')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h3>Create New Tag</h3>', html)

    # def test_new_tag(self):
    #     with app.test_client() as client:

    # def test_edit_tag_html(self):
    #     with app.test_client() as client:

    def test_tags(self):
        with app.test_client() as client:
            res = client.get('/tags')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h3>All Tags</h3>', html)

    # def editted_tag(self):
    #     with app.test_client() as client:
             
    def test_delete_tag(self):
        with app.test_client() as client:
            res = client.post('/delete-tag', data={'tag-id':'1'})

            self.assertEqual(res.status_code, 200)
        