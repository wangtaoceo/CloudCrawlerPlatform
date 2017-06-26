/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50624
Source Host           : 127.0.0.1:3306
Source Database       : crawler

Target Server Type    : MYSQL
Target Server Version : 50624
File Encoding         : 65001

Date: 2017-06-11 20:27:35
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `spider_crawler`
-- ----------------------------
DROP TABLE IF EXISTS `spider_crawler`;
CREATE TABLE `spider_crawler` (
  `crawler_id` int(11) NOT NULL AUTO_INCREMENT,
  `crawler_name` varchar(20) NOT NULL,
  `date` datetime(6) NOT NULL,
  `remark` varchar(8000) DEFAULT NULL,
  `status` varchar(20) NOT NULL DEFAULT '0',
  `user_id` varchar(20) NOT NULL,
  `workid` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`crawler_id`),
  KEY `spider_crawler_user_id_7469798e_fk_spider_user_username` (`user_id`),
  CONSTRAINT `spider_crawler_user_id_7469798e_fk_spider_user_username` FOREIGN KEY (`user_id`) REFERENCES `spider_user` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of spider_crawler
-- ----------------------------
INSERT INTO `spider_crawler` VALUES ('1', '123', '2017-04-20 22:10:48.824000', '123', '0', 'qq', null);
INSERT INTO `spider_crawler` VALUES ('2', '123', '2017-04-20 22:16:18.811000', '123', '0', '123', null);
INSERT INTO `spider_crawler` VALUES ('3', '123', '2017-04-20 22:20:07.696000', '123', '0', '123', null);
INSERT INTO `spider_crawler` VALUES ('4', '123', '2017-04-20 22:22:58.675000', '123', '0', '123', null);
INSERT INTO `spider_crawler` VALUES ('5', '123', '2017-04-20 22:29:23.617000', '123', '0', 'qq', null);
INSERT INTO `spider_crawler` VALUES ('6', '123', '2017-04-20 22:30:35.749000', '123', '0', 'qq', null);
INSERT INTO `spider_crawler` VALUES ('7', ' q', '2017-04-20 22:32:51.874000', '123', '0', 'qq', null);
INSERT INTO `spider_crawler` VALUES ('8', '123', '2017-04-20 22:38:37.027000', '123', '0', 'qq', null);
INSERT INTO `spider_crawler` VALUES ('9', '123', '2017-04-20 22:46:03.819000', '123', '0', 'qq', null);
INSERT INTO `spider_crawler` VALUES ('10', '123', '2017-04-20 22:48:22.958000', '123', '0', 'qq', null);
INSERT INTO `spider_crawler` VALUES ('11', '123', '2017-04-20 22:50:20.233000', '123', '0', 'qq', null);
INSERT INTO `spider_crawler` VALUES ('12', '123', '2017-04-20 22:53:31.845000', '123', '0', 'qq', null);
INSERT INTO `spider_crawler` VALUES ('13', '123', '2017-04-20 22:58:03.031000', '123', '0', 'qq', null);
INSERT INTO `spider_crawler` VALUES ('14', 'qqqq', '2017-04-21 09:56:18.074000', 'qq', '0', 'qq', null);
INSERT INTO `spider_crawler` VALUES ('15', '123', '2017-04-21 10:00:58.820000', '132', '0', 'qq', null);
INSERT INTO `spider_crawler` VALUES ('16', 'qqqq', '2017-04-21 10:03:18.641000', '123', '0', 'qq', null);
INSERT INTO `spider_crawler` VALUES ('17', 'city58', '2017-04-21 11:01:59.942000', '123', '0', 'username', null);
INSERT INTO `spider_crawler` VALUES ('18', 'city58', '2017-04-21 16:36:45.280000', '', '0', 'username', null);
INSERT INTO `spider_crawler` VALUES ('19', 'city58', '2017-04-21 16:37:45.333000', '', '0', 'admin', null);
INSERT INTO `spider_crawler` VALUES ('20', 'city58', '2017-04-21 18:36:13.919000', '', '0', 'qqq', null);
INSERT INTO `spider_crawler` VALUES ('21', '', '2017-04-23 16:20:19.137000', '', '0', 'aaaa', null);
INSERT INTO `spider_crawler` VALUES ('22', 'doubanxiaoshuo', '2017-04-23 16:40:48.448000', '豆瓣小说爬虫', '0', 'aaaa', null);
INSERT INTO `spider_crawler` VALUES ('23', 'doubanxiaoshuo', '2017-04-23 16:42:37.734000', '豆瓣小说爬虫', '0', 'aaaa', null);
INSERT INTO `spider_crawler` VALUES ('24', '', '2017-04-26 12:33:09.529000', '', '0', 'bbbb', null);
INSERT INTO `spider_crawler` VALUES ('25', 'doubanxiaoshuo', '2017-04-26 12:33:11.526000', '豆瓣小说爬虫', '0', 'bbbb', null);
INSERT INTO `spider_crawler` VALUES ('26', 'doubanxiaoshuo', '2017-04-26 12:34:04.285000', '豆瓣小说爬虫', '0', 'bbbb', null);
INSERT INTO `spider_crawler` VALUES ('27', '', '2017-04-26 12:40:43.749000', '', '0', 'cccc', null);
INSERT INTO `spider_crawler` VALUES ('28', 'doubanxiaoshuo', '2017-04-26 12:40:45.030000', '豆瓣小说爬虫', '0', 'cccc', null);
INSERT INTO `spider_crawler` VALUES ('29', '', '2017-04-26 12:47:09.800000', '', '0', 'dddd', null);
INSERT INTO `spider_crawler` VALUES ('30', 'doubanxiaoshuo', '2017-04-26 12:47:11.171000', '豆瓣小说爬虫', '0', 'dddd', null);
INSERT INTO `spider_crawler` VALUES ('31', '', '2017-04-26 13:02:43.896000', '', '0', 'eeee', null);
INSERT INTO `spider_crawler` VALUES ('32', 'doubanxiaoshuo', '2017-04-26 13:02:45.045000', '豆瓣小说爬虫', '0', 'eeee', null);
INSERT INTO `spider_crawler` VALUES ('33', 'zhihu', '2017-05-01 15:51:14.635000', '知乎爬虫', '0', 'eeee', '');
INSERT INTO `spider_crawler` VALUES ('34', 'qqq', '2017-05-01 16:01:43.338000', '测试', '', 'eeee', '');
INSERT INTO `spider_crawler` VALUES ('35', 'www', '2017-05-01 16:04:17.459000', '测试', '', 'eeee', '');
INSERT INTO `spider_crawler` VALUES ('36', 'eee', '2017-05-01 16:12:16.918000', '测试', '', 'eeee', '');
INSERT INTO `spider_crawler` VALUES ('37', 'doubanxiaoshuo', '2017-05-02 14:18:19.342000', '豆瓣小说爬虫', '', 'eeee', '');
INSERT INTO `spider_crawler` VALUES ('39', 'zhihu', '2017-05-02 15:14:24.142000', '知乎爬虫', '0', 'ffff', '');
INSERT INTO `spider_crawler` VALUES ('43', 'doubanxiaoshuo', '2017-05-03 12:36:31.652000', '豆瓣小说爬虫', '0', 'ffff', '');
INSERT INTO `spider_crawler` VALUES ('44', 'doubanxiaoshuo', '2017-05-03 23:21:14.372000', '豆瓣小说爬虫', '0', 'gggg', '');
INSERT INTO `spider_crawler` VALUES ('45', 'doubanxiaoshuo', '2017-05-05 15:53:16.119000', '豆瓣小说爬虫', '0', 'zzzzz', '');
INSERT INTO `spider_crawler` VALUES ('47', 'foodspider', '2017-05-19 17:04:21.851000', '大众点评美食爬虫', '0', 'ggggg', '');
INSERT INTO `spider_crawler` VALUES ('48', 'doubanxiaoshuo', '2017-05-20 09:55:30.083000', '豆瓣小说爬虫', '0', 'sssss', '');
INSERT INTO `spider_crawler` VALUES ('49', 'zhihupachong', '2017-05-20 15:34:06.702000', '知乎爬虫', '0', 'sssss', '');
INSERT INTO `spider_crawler` VALUES ('50', 'foodspider', '2017-06-11 08:18:54.375000', '大众点评美食爬虫', '0', 'ccccc', '');
INSERT INTO `spider_crawler` VALUES ('52', 'doubandianying', '2017-06-11 09:52:56.666000', '豆瓣电影爬虫', '0', 'ccccc', '');
INSERT INTO `spider_crawler` VALUES ('53', 'doubandianying', '2017-06-11 09:55:48.383000', '豆瓣电影爬虫', '0', 'vvvvv', '');
INSERT INTO `spider_crawler` VALUES ('54', 'doubandianying', '2017-06-11 10:25:50.483000', '豆瓣电影爬虫', '0', 'bbbbb', '');
INSERT INTO `spider_crawler` VALUES ('55', 'foodspider', '2017-06-11 16:07:56.448000', '大众点评美食爬虫', '0', 'jjjjj', '');
INSERT INTO `spider_crawler` VALUES ('56', 'zhihu', '2017-06-11 16:11:54.996000', '111', '0', 'jjjjj', '');
INSERT INTO `spider_crawler` VALUES ('57', 'doubanxiaoshuo', '2017-06-11 16:15:20.618000', '豆瓣小说爬虫', '0', 'jjjjj', '');
INSERT INTO `spider_crawler` VALUES ('58', 'doubandianying', '2017-06-11 16:21:14.186000', '豆瓣电影爬虫', '0', 'jjjjj', '');
INSERT INTO `spider_crawler` VALUES ('59', 'doubanxiaoshuo', '2017-06-11 17:20:38.278000', '豆瓣小说爬虫', '0', 'glone', '');
INSERT INTO `spider_crawler` VALUES ('60', 'foodspider', '2017-06-11 17:25:49.294000', '大众点评美食爬虫', '0', 'glone', '');

-- ----------------------------
-- Table structure for `spider_mycrawler`
-- ----------------------------
DROP TABLE IF EXISTS `spider_mycrawler`;
CREATE TABLE `spider_mycrawler` (
  `crawler_id` int(11) NOT NULL AUTO_INCREMENT,
  `crawler_name` varchar(20) NOT NULL,
  `spiderfile` varchar(50) NOT NULL,
  `remark` varchar(8000) DEFAULT NULL,
  PRIMARY KEY (`crawler_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of spider_mycrawler
-- ----------------------------
INSERT INTO `spider_mycrawler` VALUES ('1', '豆瓣小说爬虫', 'doubanxiaoshuo', '豆瓣小说爬虫');
INSERT INTO `spider_mycrawler` VALUES ('2', '大众点评美食爬虫', 'foodspider', '大众点评美食爬虫');
INSERT INTO `spider_mycrawler` VALUES ('3', '智联招聘爬虫', 'zhilianzhaopin', '智联招聘爬虫');
INSERT INTO `spider_mycrawler` VALUES ('4', '豆瓣电影爬虫', 'doubandianying', '豆瓣电影爬虫');
INSERT INTO `spider_mycrawler` VALUES ('5', '大众点评娱乐爬虫', 'yulespider', '大众点评娱乐爬虫');

-- ----------------------------
-- Table structure for `spider_user`
-- ----------------------------
DROP TABLE IF EXISTS `spider_user`;
CREATE TABLE `spider_user` (
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `date` datetime(6) NOT NULL,
  `crawler_num` int(11) NOT NULL,
  `crawler_num_now` int(11) NOT NULL,
  `id` int(11) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of spider_user
-- ----------------------------
INSERT INTO `spider_user` VALUES ('123', '123', 'limitlesss@163.com', '2017-04-20 21:26:40.038000', '3', '0', '0');
INSERT INTO `spider_user` VALUES ('aaaa', 'aaaa', '123@123.com', '2017-04-23 16:20:06.042000', '3', '0', '0');
INSERT INTO `spider_user` VALUES ('abc', '1231', '', '2017-05-03 23:20:25.542000', '0', '0', '0');
INSERT INTO `spider_user` VALUES ('admin', 'qq', '123@123.com', '2017-04-21 16:37:38.093000', '1', '0', '0');
INSERT INTO `spider_user` VALUES ('bbbb', 'bb', '123@123.com', '2017-04-26 12:32:56.178000', '3', '0', '0');
INSERT INTO `spider_user` VALUES ('bbbbb', 'bbbbb', 'limitlesss@163.com', '2017-06-11 10:25:44.733000', '1', '0', '0');
INSERT INTO `spider_user` VALUES ('cccc', 'cc', '123@123.com', '2017-04-26 12:40:38.634000', '2', '0', '0');
INSERT INTO `spider_user` VALUES ('ccccc', 'ccccc', 'limitlesss@163.com', '2017-06-11 08:18:40.112000', '2', '0', '0');
INSERT INTO `spider_user` VALUES ('dddd', 'dd', '123@123.com', '2017-04-26 12:47:06.822000', '2', '0', '0');
INSERT INTO `spider_user` VALUES ('eeee', 'ee', '123@123.com', '2017-04-26 13:02:40.368000', '7', '0', '0');
INSERT INTO `spider_user` VALUES ('ffff', 'ffff', 'fff@fff.com', '2017-05-02 14:31:01.820000', '2', '0', '0');
INSERT INTO `spider_user` VALUES ('gggg', 'gggg', 'gggg', '2017-05-03 23:21:00.169000', '1', '0', '0');
INSERT INTO `spider_user` VALUES ('ggggg', 'gg', 'limitlesss@163.com', '2017-05-19 16:56:25.776000', '1', '0', '0');
INSERT INTO `spider_user` VALUES ('glone', '1', '123@163.com', '2017-06-11 17:20:01.849000', '2', '0', '0');
INSERT INTO `spider_user` VALUES ('jjjjj', 'jjjjj', 'limitlesss@163.com', '2017-06-11 16:07:41.238000', '4', '0', '0');
INSERT INTO `spider_user` VALUES ('qq', 'qq', '123@123.com', '2017-04-20 22:05:40.935000', '14', '0', '0');
INSERT INTO `spider_user` VALUES ('qqq', 'qq', '123@123.com', '2017-04-21 18:36:03.939000', '1', '0', '0');
INSERT INTO `spider_user` VALUES ('sssss', 'ssss', 'for_dream2008@163.co', '2017-05-20 09:35:24.276000', '2', '0', '0');
INSERT INTO `spider_user` VALUES ('username', 'qq', 'qq@qq.com', '2017-04-21 11:00:12.726000', '2', '0', '0');
INSERT INTO `spider_user` VALUES ('vvvvv', 'vvvvv', 'limitlesss@163.com', '2017-06-11 09:55:42.711000', '1', '0', '0');
INSERT INTO `spider_user` VALUES ('zzzzz', 'zz', '123@123.com', '2017-05-05 15:52:48.502000', '1', '0', '0');
