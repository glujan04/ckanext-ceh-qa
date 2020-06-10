import copy
from ckan.plugins import toolkit as tk
import lib
from ckan import model


def qa_openness_stars_resource_html(resource):
    qa = resource.get('qa')
    qa = {'openness_score': 3, 'openness_score_reason': 'Content of file appeared to be format \"CSV\" which receives openness score: 3.',
               'updated': '2015-11-19T16:54:49.480393'}
    if not qa:
        return tk.literal('<!-- No qa info for this resource -->')
    if not isinstance(qa, dict):
        return tk.literal('<!-- QA info was of the wrong type -->')

    # Take a copy of the qa dict, because weirdly the renderer appears to add
    # keys to it like _ and app_globals. This is bad because when it comes to
    # render the debug in the footer those extra keys take about 30s to render,
    # for some reason.
    extra_vars = copy.deepcopy(qa)
    return tk.literal(
        tk.render('qa/openness_stars.html',
                  extra_vars=extra_vars))


def qa_openness_stars_dataset_html(dataset):
    qa = dataset.get('qa')
    qa = {'openness_score': 3, 'openness_score_reason': 'Content of file appeared to be format \"CSV\" which receives openness score: 3.',
               'updated': '2015-11-19T16:54:49.480393'}
    print(dataset)
    print(qa)
    if not qa:
        return tk.literal('<!-- No qa info for this dataset -->')
    if not isinstance(qa, dict):
        return tk.literal('<!-- QA info was of the wrong type -->')
    extra_vars = copy.deepcopy(qa)
    return tk.literal(
        tk.render('qa/openness_stars_brief.html',
                  extra_vars=extra_vars))


def qa_openness_stars_dataset2_html(dataset):
    qa = dataset.get('qa')
    qa = {'openness_score': 3, 'openness_score_reason': 'Content of file appeared to be format \"CSV\" which receives openness score: 3.',
               'updated': '2015-11-19T16:54:49.480393'}
    #Pregunta si es de tipo dataset
    field_name = getattr(dataset, 'type')
    #valida que el dataset no sea de tipo harvest
    if field_name!='dataset':
        return tk.literal('<!-- No qa info for this dataset -->')
    #se obtienen los formatos disponibles
    jsonFormats_ = lib.resource_format_scores()
    #for item in jsonFormats_:
    #   print jsonFormats_[item]
    id_ = getattr(dataset, 'id')
    pkg = model.Package.get(id_)
    print 'Package %s %s' % (pkg.name, pkg.id)
    _RESOURCES = {}
    for res in pkg.resources:
        #print res format
        format_ = getattr(res, 'format')
        #if format_ in _RESOURCES:
        #    raise ValueError('Formato duplicado %s' % (format_))
        _RESOURCES[format_] = jsonFormats_[format_]
    print _RESOURCES
    if not qa:
        return tk.literal('<!-- No qa info for this dataset -->')
    if not isinstance(qa, dict):
        return tk.literal('<!-- QA info was of the wrong type -->')

    # Take a copy of the qa dict, because weirdly the renderer appears to add
    # keys to it like _ and app_globals. This is bad because when it comes to
    # render the debug in the footer those extra keys take about 30s to render,
    # for some reason.
    extra_vars = copy.deepcopy(qa)
    return tk.literal(
        tk.render('qa/openness_stars.html',
                  extra_vars=extra_vars))
