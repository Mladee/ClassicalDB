from django.shortcuts import render, redirect, get_object_or_404
from muzica_clasica.forms import *
from django.contrib import messages


def index(request):
    return render(request, 'muzica_clasica/home.html')


def composers_view(request):
    composers_list = Compozitori.objects.order_by('stil')
    name_dict = {'composers': composers_list}
    return render(request, 'muzica_clasica/composers.html', context=name_dict)


def _composition_view(request):
    compositions_list = Compozitii.objects.order_by('an_aparitie')
    name_dict = {'composition': compositions_list}
    return render(request, 'muzica_clasica/compositions.html',
                  context=name_dict)


def _catalogues_view(request):
    catalogues_list = Cataloage.objects.order_by('compozitor')
    name_dict = {'catalogues': catalogues_list}
    return render(request, 'muzica_clasica/catalogues.html', context=name_dict)


def add_composer(request):
    if request.method == 'POST':
        composer_form = ComposerForm(request.POST)
        if composer_form.is_valid():
            composer_form.save()
            messages.success(request, 'Composer added')
        else:
            messages.error(request, 'Error saving form')

        return redirect('/classicaldb/composers')

    composer_form = ComposerForm()
    composers = Compozitori.objects.all()
    return render(request, 'muzica_clasica/composer_add.html',
                  context={'composer_form': composer_form,
                           'composers': composers})


def add_composition(request):
    if request.method == 'POST':
        composition_form = CompositionForm(request.POST)
        if composition_form.is_valid():
            composition_form.save()
            messages.success(request, 'Composition added')
        else:
            messages.error(request, 'Error saving form')

        return redirect("/classicaldb/home")
    composition_form = CompositionForm()
    return render(request, 'muzica_clasica/composition_add.html',
                  context={'composition_form': composition_form})


def add_catalogue(request):
    if request.method == 'POST':
        catalogue_form = CatalogueForm(request.POST)
        if catalogue_form.is_valid():
            catalogue_form.save()
            messages.success(request, 'Composition added')
        else:
            messages.error(request, 'Error saving form')
        return redirect('/classicaldb/')
    catalogue_form = CatalogueForm()
    return render(request, 'muzica_clasica/catalogue_add.html',
                  context={'catalogue_form': catalogue_form})


def update_composer(request, id):
    composer = get_object_or_404(Compozitori, id=id)
    if request.method == 'POST':
        update_form = ComposerForm(request.POST, instance=composer)
        if update_form.is_valid():
            update_form.save()
            return redirect('/classicaldb/composers')
    else:
        update_form = ComposerForm(instance=composer)

    update_form = ComposerForm()
    return render(request, 'muzica_clasica/composer_update.html',
                  {
                      'form': update_form,
                      'composer': composer,
                  })


def update_composition(request, id):
    composition = get_object_or_404(Compozitii, id=id)
    if request.method == 'POST':
        update_form = CompositionForm(request.POST, instance=composition)
        if update_form.is_valid():
            update_form.save()
            return redirect('/classicaldb/composers')
    else:
        update_form = CompositionForm(instance=composition)

    update_form = CompositionForm()
    return render(request, 'muzica_clasica/composition_update.html',
                  {
                      'form': update_form,
                      'composition': composition,
                  })


def update_catalogue(request,id):
    catalogue = get_object_or_404(Cataloage, id=id)
    if request.method == 'POST':
        update_form = CatalogueForm(request.POST, instance=catalogue)
        if update_form.is_valid():
            update_form.save()
            return redirect('/classicaldb/')
    else:
        update_form = CatalogueForm(instance=catalogue)

    update_form = CatalogueForm()
    return render(request, 'muzica_clasica/catalogue_update.html',
                  {
                      'form': update_form,
                      'catalogue': catalogue,
                  })


def delete_composer(request, id):
    composer = get_object_or_404(Compozitori, id=id)
    if request.method == 'POST':
        delete_form = ComposerDeleteForm(request.POST, instance=composer)
        if delete_form.is_valid():
            composer.delete()
            return redirect('/classicaldb/')
    else:
        delete_form = ComposerDeleteForm(instance=composer)

    delete_form = ComposerDeleteForm()
    return render(request, 'muzica_clasica/composer_delete.html',
                  {
                      'form': delete_form,
                      'composer': composer,
                  })


def delete_composition(request, id):
    composition = get_object_or_404(Compozitii, id=id)
    if request.method == 'POST':
        delete_form = CompositionDeleteForm(request.POST, instance=composition)
        if delete_form.is_valid():
            composition.delete()
            return redirect('/classicaldb/')
    else:
        delete_form = CompositionDeleteForm(instance=composition)

    delete_form = CompositionDeleteForm()
    return render(request, 'muzica_clasica/composition_delete.html',
                  {
                      'form': delete_form,
                      'composition': composition,
                  })


def delete_catalogue(request, id):
    catalogue = get_object_or_404(Cataloage, id=id)
    if request.method == 'POST':
        delete_form = CatalogueDeleteForm(request.POST, instance=catalogue)
        if delete_form.is_valid():
            catalogue.delete()
            return redirect('/classicaldb/composers')
    else:
        delete_form = CatalogueDeleteForm(instance=catalogue)

    delete_form = CatalogueDeleteForm()
    return render(request, 'muzica_clasica/catalogue_delete.html',
                  {
                      'form': delete_form,
                      'catalogue': catalogue,
                  })


def compositions_view(request, id):
    composition_list = Compozitii.objects.filter(
        cataloage__compozitor=id).order_by('an_aparitie')
    composition_dict = {'composition': composition_list}
    return render(request, 'muzica_clasica/composer_compositions.html',
                  context=composition_dict)


def catalogues_view(request, id):
    catalogue_list = Cataloage.objects.filter(
        compozitie__cataloage__compozitor_id=id).order_by('simbol')
    catalogue_dict = {'catalogues': catalogue_list}
    return render(request, 'muzica_clasica/composer_catalogues.html',
                  context=catalogue_dict)