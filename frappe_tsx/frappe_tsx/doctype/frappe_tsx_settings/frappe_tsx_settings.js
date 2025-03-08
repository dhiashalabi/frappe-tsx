// Copyright (c) 2025, DHia A. SHalabi and contributors
// For license information, please see license.txt

frappe.ui.form.on("Frappe TSX Settings", {
	generate_child_tables(frm) {
		if (frm.doc.generate_child_tables) {
			frappe.confirm(
				"Enabling this option will also generate TypeScript definitions for child tables. Are you sure you want to proceed?",
				() => {
					frm.set_value("generate_child_tables", 1);
				},
				() => {
					frm.set_value("generate_child_tables", 0);
				}
			);
		}
	}
});

frappe.ui.form.on("Frappe TSX Settings App", {
	form_render(frm, cdt, cdn) {
		if (frm.doc.app_names) {
			frm.fields_dict.apps.grid.update_docfield_property("app_name", "options", frm.doc.app_names);
		}
	},
	apps_add(frm, cdt, cdn) {
		frappe.xcall("frappe.core.doctype.module_def.module_def.get_installed_apps").then((r) => {
			frm.doc.app_names = JSON.parse(r);
			frm.fields_dict.apps.grid.update_docfield_property("app_name", "options", frm.doc.app_names);
		});
	}
});
