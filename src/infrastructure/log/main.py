# Thanks https://github.com/SamWarden/user_service

import logging.config

import structlog
from structlog.processors import CallsiteParameter, CallsiteParameterAdder

from .config import Config
from .processors import get_render_processor


def configure_logging(config: Config) -> None:
    common_processors = (
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.ExtraAdder(),
        structlog.dev.set_exc_info,
        structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S.%f", utc=True),
        structlog.contextvars.merge_contextvars,
        structlog.processors.dict_tracebacks,
        CallsiteParameterAdder(
            (
                CallsiteParameter.FUNC_NAME,
                CallsiteParameter.LINENO,
            )
        ),
    )
    structlog_processors = (
        structlog.processors.StackInfoRenderer(),
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.UnicodeDecoder(),  # convert bytes to str
        # structlog.stdlib.render_to_log_kwargs,
        structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        # structlog.processors.format_exc_info,  # print exceptions from event dict
    )
    logging_processors = (structlog.stdlib.ProcessorFormatter.remove_processors_meta,)
    logging_console_processors = (
        *logging_processors,
        get_render_processor(render_json_logs=config.render_json_logs, colors=True),
    )

    handler = logging.StreamHandler()
    handler.set_name("default")
    handler.setLevel(config.level)
    console_formatter = structlog.stdlib.ProcessorFormatter(
        foreign_pre_chain=common_processors,  # type: ignore
        processors=logging_console_processors,
    )
    handler.setFormatter(console_formatter)

    handlers = [handler]
    if config.path:
        config.path.parent.mkdir(parents=True, exist_ok=True)
        log_path = config.path / "logs.log" if config.path.is_dir() else config.path

        logging_file_processors = (
            *logging_processors,
            get_render_processor(
                render_json_logs=config.render_json_logs, colors=False
            ),
        )

        file_handler = logging.FileHandler(log_path)
        file_handler.set_name("file")
        file_handler.setLevel(config.level)
        file_formatter = structlog.stdlib.ProcessorFormatter(
            foreign_pre_chain=common_processors,  # type: ignore
            processors=logging_file_processors,
        )
        file_handler.setFormatter(file_formatter)
        handlers.append(file_handler)  # type: ignore

    logging.basicConfig(handlers=handlers, level=config.level)

    structlog.configure(
        processors=common_processors + structlog_processors,
        logger_factory=structlog.stdlib.LoggerFactory(),
        # wrapper_class=structlog.stdlib.AsyncBoundLoggerd,  # type: ignore  # noqa
        wrapper_class=structlog.stdlib.BoundLogger,  # type: ignore  # noqa
        cache_logger_on_first_use=True,
    )
