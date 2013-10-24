from pelican import signals
from pelican.paginator import Paginator
from pelican.writers import Writer, logger
from pelican.generators import ArticlesGenerator
import locale
import os

class NewWriter(Writer):
	def __init__(self, output_path, settings = None):
		super(NewWriter, self).__init__(output_path, settings)

	def write_file(self, name, template, context, relative_urls=False, paginated=None, override_output=False, **kwargs):
		if name is False:
				return
		elif not name:
				# other stuff, just return for now
				return
		def _write_file(template, localcontext, output_path, name, override):
				"""Render the template write the file."""
				old_locale = locale.setlocale(locale.LC_ALL)
				locale.setlocale(locale.LC_ALL, str('C'))
				try:
						output = template.render(localcontext)
				finally:
						locale.setlocale(locale.LC_ALL, old_locale)
						path = os.path.join(output_path, name)
				try:
						os.makedirs(os.path.dirname(path))
				except Exception:
						pass

				with self._open_w(path, 'utf-8', override=override) as f:
						f.write(output)
				logger.info('writing {}'.format(path))

				# Send a signal to say we're writing a file with some specific
				# local context.
				signals.content_written.send(path, context=localcontext)

		localcontext = context.copy()
		if relative_urls:
				relative_url = path_to_url(get_relative_path(name))
				context['localsiteurl'] = relative_url
				localcontext['SITEURL'] = relative_url

		localcontext['output_file'] = name
		localcontext.update(kwargs)

		# check paginated
		paginated = paginated or {}
		if paginated:
				name_root = os.path.splitext(name)[0]

				# pagination needed, init paginators
				paginators = {}
				for key in paginated.keys():
						object_list = paginated[key]
						object_list = [x for x in object_list if not hasattr(x, 'type')]

						paginators[key] = Paginator(
								name_root,
								object_list,
								self.settings,
						)

				# generated pages, and write
				for page_num in range(list(paginators.values())[0].num_pages):
						paginated_localcontext = localcontext.copy()
						for key in paginators.keys():
								paginator = paginators[key]
								previous_page = paginator.page(page_num) \
												if page_num > 0 else None
								page = paginator.page(page_num + 1)
								next_page = paginator.page(page_num + 2) \
												if page_num + 1 < paginator.num_pages else None
								paginated_localcontext.update(
												{'%s_paginator' % key: paginator,
												 '%s_page' % key: page,
												 '%s_previous_page' % key: previous_page,
												 '%s_next_page' % key: next_page})

						_write_file(template, paginated_localcontext, self.output_path,
												page.save_as, override_output)
		else:
				# no pagination
				_write_file(template, localcontext, self.output_path, name,
										override_output)
class NewArticlesGenerator(ArticlesGenerator):
	"""
		generator the articles
	"""
	def __init__(self, *args, **kwargs):
		super(NewArticlesGenerator, self).__init__(*args, **kwargs)
	
	def generate_output(self, writer):
		newwriter = NewWriter(writer.output_path, writer.settings)
		self.generate_pages(newwriter)

def get_generators(generators):
		"""
				decorator
		"""
		return NewArticlesGenerator

def register():
		"""
				register for the pelican
		"""
		signals.get_generators.connect(get_generators)


