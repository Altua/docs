"""Build the four guide PDFs and complete follow-up checklist locally."""
from pathlib import Path
import runpy
from build_customer_guide import build

for name, label in [
    ('solution-overview', 'Solution overview'),
    ('it-security-overview', 'IT and security overview'),
    ('getting-started', 'Getting started'),
    ('organization-integration', 'Organization integration guide'),
]:
    build(source_name=f'grunt-one-{name}.md', label=label)

runpy.run_path(str(Path(__file__).with_name('build_follow_up_checklist.py')), run_name='__main__')
