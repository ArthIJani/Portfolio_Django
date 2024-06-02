# In your filters.py (or a separate app)
from django import template

register = template.Library()

@register.filter(name='truncatewords')
def truncatewords(text, num_words):
  """
  Truncates a text string to a specific number of words.
  """
  words = text.split()[:num_words]
  return ' '.join(words) + (len(words) < len(text.split()) and '...' or '')
