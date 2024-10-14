import unittest
from loaders.pdf_loader import PDFLoader
from extractors.data_extract import DataExtractor

class TestExtractor(unittest.TestCase):

    def setUp(self):
        # Create or define paths to test files
        self.sample_pdf = 'sample.pdf'  # Path to your valid test PDF
        self.empty_pdf = 'empty.pdf'  # Path to your empty test PDF
        # self.large_pdf = 'tests/test_files/large_sample.pdf'  # Path to your large test PDF
        # self.protected_pdf = 'tests/test_files/protected.pdf'  # Path to your password-protected PDF
        # self.pdf_no_links = 'tests/test_files/pdf_no_links.pdf'  # Path to your test PDF with no links
        # self.pdf_no_images = 'tests/test_files/pdf_no_images.pdf'  # Path to your test PDF with no images
        # self.pdf_no_tables = 'tests/test_files/pdf_no_tables.pdf'  # Path to your test PDF with no tables

    def test_pdf_extraction(self):
        loader = PDFLoader(self.sample_pdf)
        extractor = DataExtractor(loader)
        text_data = extractor.extract_text()
        self.assertTrue(len(text_data) > 0)

    def test_empty_pdf(self):
        loader = PDFLoader(self.empty_pdf)
        extractor = DataExtractor(loader)
        text_data = extractor.extract_text()
        self.assertEqual(text_data, '')  # Ensure it returns an empty string

    # def test_file_not_found(self):
    #     with self.assertRaises(FileNotFoundError):
    #         loader = PDFLoader('non_existent.pdf')
    #         extractor = DataExtractor(loader)
    #         extractor.extract_text()

    # def test_pdf_with_no_links(self):
    #     loader = PDFLoader(self.pdf_no_links)
    #     extractor = DataExtractor(loader)
    #     links = extractor.extract_links()
    #     self.assertEqual(links, [])  # Ensure it returns an empty list if no links are present

    # def test_pdf_with_no_images(self):
    #     loader = PDFLoader(self.pdf_no_images)
    #     extractor = DataExtractor(loader)
    #     images = extractor.extract_images()
    #     self.assertEqual(images, [])  # Ensure it returns an empty list if no images are present

    # def test_pdf_with_no_tables(self):
    #     loader = PDFLoader(self.pdf_no_tables)
    #     extractor = DataExtractor(loader)
    #     tables = extractor.extract_tables()
    #     self.assertEqual(tables, [])  # Ensure it returns an empty list if no tables are present



if __name__ == '__main__':
    unittest.main()

