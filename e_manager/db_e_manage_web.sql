/*
Navicat MySQL Data Transfer

Source Server         : user
Source Server Version : 50721
Source Host           : localhost:3306
Source Database       : db_e_manage_web

Target Server Type    : MYSQL
Target Server Version : 50721
File Encoding         : 65001

Date: 2020-03-28 14:48:23
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `password` varchar(32) NOT NULL,
  `status` int(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES ('1', 'admin', 'admin', '1');

-- ----------------------------
-- Table structure for college
-- ----------------------------
DROP TABLE IF EXISTS `college`;
CREATE TABLE `college` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `location` varchar(128) DEFAULT NULL,
  `dormitory_manager_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dormitory_id_fk` (`dormitory_manager_id`),
  CONSTRAINT `college_ibfk_1` FOREIGN KEY (`dormitory_manager_id`) REFERENCES `department_manager` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of college
-- ----------------------------
INSERT INTO `college` VALUES ('1', '001', '计算机', '7');
INSERT INTO `college` VALUES ('2', '004', '数学与统计学院', '18');
INSERT INTO `college` VALUES ('12', '123', '教育学院', '18');

-- ----------------------------
-- Table structure for department_manager
-- ----------------------------
DROP TABLE IF EXISTS `department_manager`;
CREATE TABLE `department_manager` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sn` varchar(32) NOT NULL,
  `name` varchar(32) NOT NULL,
  `password` varchar(32) NOT NULL,
  `sex` varchar(8) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of department_manager
-- ----------------------------
INSERT INTO `department_manager` VALUES ('7', 'S1537881909951', '张杰', '123456', '学校');
INSERT INTO `department_manager` VALUES ('18', 'S1537965298839', '张思思', '123456', '教育局');
INSERT INTO `department_manager` VALUES ('19', 'DM1585369412530', '周甜甜', '45678', '学校');

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sn` varchar(32) NOT NULL,
  `name` varchar(32) NOT NULL,
  `password` varchar(32) NOT NULL,
  `sex` varchar(8) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES ('7', 'S1537881909951', '张三', '123', 'not');
INSERT INTO `student` VALUES ('8', 'S1537881928894', '李四', '123456', 'not');
INSERT INTO `student` VALUES ('9', 'S1537882773788', '马冬梅', '123456789', 'yes');
INSERT INTO `student` VALUES ('18', 'S1538216365262', '晓明', '123', 'not');
INSERT INTO `student` VALUES ('19', 'S1538216374036', '张军', '123456', 'not');
INSERT INTO `student` VALUES ('20', 'S1538216388860', '黎明', '123456', 'not');
INSERT INTO `student` VALUES ('22', 'S1585371244322', '李现', '8765', 'yes');
INSERT INTO `student` VALUES ('23', 'S1585375881892', '张雪玉', '987', 'yes');
INSERT INTO `student` VALUES ('24', 'S1585376388506', '刘学友', '4567', 'not');
