from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from category.models import Category
logger = get_task_logger(__name__)


@periodic_task(run_every=(crontab(minute=0, hour=0)), name="activate_categories", ignore_result=True)
def activate_categories():
    logger.info("Updated Successfully")
    Category.objects.filter(is_active=False).update(is_active=True)
