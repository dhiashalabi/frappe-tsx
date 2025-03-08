import click
import frappe
from frappe.commands import pass_context
from frappe.exceptions import SiteNotSpecifiedError

from frappe_tsx.frappe_tsx.type_generator import generate_types_for_doctype, generate_types_for_module


@click.command("generate-types-for-doctype")
@click.option("--app", prompt="App Name")
@click.option("--doctype", prompt="Doctype Name")
@click.option(
	"--generate_child_tables",
	default=False,
	is_flag=True,
	prompt="Do you want to generate types for child tables too?",
	help="It will generate Types for child tables includes in the doctype",
)
@click.option(
	"--custom_fields",
	default=False,
	is_flag=True,
	prompt="Do you want to generate types for custom fields too if exists?",
	help="It will generate Types for custom fields includes in the doctype",
)
@pass_context
def generate_types_file_from_doctype(context, app, doctype, generate_child_tables, custom_fields):
	"""Generate types file from doctype

	Args:
		context: Frappe context
		app: App name
		doctype: Doctype name
		generate_child_tables: Generate types for child tables
		custom_fields: Generate types for custom fields

	Example:
		>>> frappe-tsx generate-types-for-doctype --app=frappe --doctype=DocType
		>>> frappe-tsx generate-types-for-doctype --app=frappe --doctype=DocType --generate-child-tables
		>>> frappe-tsx generate-types-for-doctype --app=frappe --doctype=DocType --custom-fields
		>>> frappe-tsx generate-types-for-doctype --app=frappe --doctype=DocType --generate-child-tables --custom-fields

	Note:
		You can also pass multiple sites with --site flag
		>>> frappe-tsx generate-types-for-doctype --app=frappe --doctype=DocType --generate-child-tables --custom-fields --site=site1 --site=site2

	Raises:
		SiteNotSpecifiedError: If no site is specified
	"""
	if not app:
		click.echo("Please provide an app with --app")
		return

	print(f"Generating types file for {doctype} in {app}")

	for site in context.sites:
		frappe.connect(site=site)
		try:
			generate_types_for_doctype(doctype, app, generate_child_tables, custom_fields)
		finally:
			frappe.destroy()

	if not context.sites:
		raise frappe.SiteNotSpecifiedError


@click.command("generate-types-for-module")
@click.option("--app", prompt="App Name")
@click.option("--module", prompt="Module Name")
@click.option(
	"--generate_child_tables",
	default=False,
	is_flag=True,
	prompt="Do you want to generate types for child tables too?",
	help="It will generate Types for child tables includes in the doctype",
)
@pass_context
def generate_types_file_from_module(context, app, module, generate_child_tables):
	"""Generate types file from module

	Args:
		context: Frappe context
		app: App name
		module: Module name
		generate_child_tables: Generate types for child tables

	Example:
		>>> frappe-tsx generate-types-for-module --app=frappe --module=frappe
		>>> frappe-tsx generate-types-for-module --app=frappe --module=frappe --generate-child-tables

	Note:
		You can also pass multiple sites with --site flag
		>>> frappe-tsx generate-types-for-module --app=frappe --module=frappe --generate-child-tables --site=site1 --site=site2

	Raises:
		SiteNotSpecifiedError: If no site is specified
	"""
	if not app:
		click.echo("Please provide an app with --app")
		return

	print(f"Generating types file for {module} in {app}")

	for site in context.sites:
		frappe.connect(site=site)
		try:
			generate_types_for_module(module, app, generate_child_tables)
		finally:
			frappe.destroy()

	if not context.sites:
		raise SiteNotSpecifiedError


commands = [generate_types_file_from_doctype, generate_types_file_from_module]
