from loguru import logger
import datetime
import os
if __name__ == '__main__':

    log_file_name = os.getcwd()+'/logger/log.log'  # linux路径 我给的相对路径

    logger.add(log_file_name,  # 可以带有路径 没路径的logger会自己创建
               rotation='100 KB',  # 按文件大小切割日志
               enqueue=True,  # 这使得进程安全
               colorize=True,  # 彩色显示 只要系统支持
               level='WARNING')  # 这个级别以上的才会被写入文件，包含这个级别的

    ziduan = {i: 123432 for i in range(10)}

    for i in range(1000):
        logger.debug(ziduan)
        logger.info(ziduan)
        logger.warning(ziduan)
        logger.error(ziduan)
        logger.critical(ziduan)
        logger.critical(datetime.datetime)
