from django.test import TestCase
from django.core.urlresolvers import reverse
import format_fixture

from .models import Mineral
# Create your tests here.


class MineralModelTests(TestCase):
    def tearDown(self):
        Mineral.objects.filter(category='test').delete()

    def test_mineral_creation(self):
        test_mineral = Mineral.objects.create(
            name='test-name1',
            image_filename='test.jpg',
            image_caption='test1',
            category='test1',
            formula='test1',
            strunz_classification='test1',
            crystal_system='test1',
            unit_cell='test1',
            color='test1',
            crystal_symmetry='test1',
            cleavage='test1',
            mohs_scale_hardness='test1',
            luster='test1',
            streak='test1',
            diaphaneity='test1',
            optical_properties='test1',
            refractive_index='test1',
            crystal_habit='test1',
            specific_gravity='test1'
        )
        self.assertTrue(test_mineral.name == 'test-name1')
        name = str(test_mineral)
        self.assertEqual(name, test_mineral.name)


class MineralViewsTests(TestCase):
    def setUp(self):
        self.test_mineral1 = Mineral.objects.create(
            name='test-name1',
            image_filename='test.jpg',
            image_caption='test1',
            category='test1',
            formula='test1',
            strunz_classification='test1',
            crystal_system='test1',
            unit_cell='test1',
            color='test1',
            crystal_symmetry='test1',
            cleavage='test1',
            mohs_scale_hardness='test1',
            luster='test1',
            streak='test1',
            diaphaneity='test1',
            optical_properties='test1',
            refractive_index='test1',
            crystal_habit='test1',
            specific_gravity='test1'
        )
        self.test_mineral2 = Mineral.objects.create(
            name='test-name2',
            image_filename='test.jpg',
            image_caption='test2',
            category='test2',
            formula='test2',
            strunz_classification='test2',
            crystal_system='test2',
            unit_cell='test2',
            color='test2',
            crystal_symmetry='test2',
            cleavage='test2',
            mohs_scale_hardness='test2',
            luster='test2',
            streak='test2',
            diaphaneity='test2',
            optical_properties='test2',
            refractive_index='test2',
            crystal_habit='test2',
            specific_gravity='test2'
        )
        self.test_mineral3 = Mineral.objects.create(
            name='test-name3',
            image_filename='test3.jpg',
            image_caption='test3',
            category='test3',
            formula='test3',
            strunz_classification='test3',
            crystal_system='test3',
            unit_cell='test3',
            color='test3',
            crystal_symmetry='test3',
            cleavage='test3',
            mohs_scale_hardness='test3',
            luster='test3',
            streak='test3',
            diaphaneity='test3',
            optical_properties='test3',
            refractive_index='test3',
            crystal_habit='test3',
            specific_gravity='test3'
        )

    def test_index_view(self):
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.test_mineral1, resp.context['minerals'])
        self.assertIn(self.test_mineral2, resp.context['minerals'])

    def test_detail_view(self):
        resp = self.client.get(reverse('minerals:detail', kwargs={'name': self.test_mineral1.name}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.test_mineral1, resp.context['mineral'])

    def test_random_view(self):
        resp = self.client.get(reverse('minerals:random'))
        self.assertEqual(resp.status_code, 200)
        random_mineral = resp.context['mineral']
        self.assertIn('test', random_mineral.category)


class ScriptsTest(TestCase):
    def test_load_database(self):
        format_fixture.populate_database()
        mineral = Mineral.objects.get(name="Mascagnite")
        self.assertEqual(mineral.category, "Sulfate")

    def test_others_run(self):
        format_fixture.find_duplicates()
        format_fixture.most_common()
