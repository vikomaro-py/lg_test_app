from core.pipelines import PIPELINES, DEFAULT_PIPELINE, DEFAULT_SOURCE


def run(data, pipeline_name='default', source_type='default'):
    """
    Starts CLI app
    :param data: path to csv according to pipeline
    :param pipeline_name:
    :param source_type:
    :return: result of last function in pipline
    """
    source = PIPELINES.get(pipeline_name, DEFAULT_SOURCE)
    pipeline = source.get(source_type, DEFAULT_PIPELINE)
    result = data
    for step in pipeline.keys():
        result = pipeline[step](result).run()
    return result
