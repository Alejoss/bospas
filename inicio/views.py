from django.views.generic import TemplateView


class ViewHome(TemplateView):
	template_name = "inicio/home.html"


class ViewAbout(TemplateView):
	template_name = "inicio/about.html"	


class ViewGalery(TemplateView):
	template_name = "inicio/gallery.html"


class ViewInfo(TemplateView):
	template_name = "inicio/info.html"

class ViewContact(TemplateView):
	template_name = "inicio/contact.html"
