def junit(fileData):
    content = '''package '''+fileData['path']+'''service.impl;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
import org.springframework.test.context.web.WebAppConfiguration;
import org.springframework.transaction.annotation.Transactional;

import klago.util.model.ERPUserInfo;
import klago.util.model.SessionInfo;
import klago.util.model.UCUserInfo;

import '''+fileData['path']+'''service.I'''+fileData['menuCodeU']+'''Service;
// JunitUtil import 경로 미정

/**
 * Name : '''+fileData['menuCodeU']+'''ServiceTest
 * Title :
 * 
 * <pre>
 * <b>History :</b>
 * </pre>
 * 
 * @author :
 * @date : 
 * @return
 */

@Transactional
@WebAppConfiguration
// Spring의 context 파일을 테스트시에도 로딩하기 위해 아래의 @ContextConfiguration 을 사용한다
// WebContent > WEB-INF -> web.xml의 contextConfigLocation의 classpath를 지정
@ContextConfiguration(locations = { "file:src/test/resources/config/spring/*.xml" })
// JUnit에 내장된 러너 대신 Spring에 맞는 SpringJUnit4 러너를 설정한다
@RunWith(SpringJUnit4ClassRunner.class)

public class '''+fileData['menuCodeU']+'''ServiceTest {

    @Autowired
    I'''+fileData['menuCodeU']+'''Service service;


    @SuppressWarnings ( "unused" )
    private Logger logger = LoggerFactory.getLogger('''+fileData['menuCodeU']+'''ServiceTest.class);
    private JunitUtils util = new JunitUtils();
    @SuppressWarnings ( "unused" )
    private ERPUserInfo erpUserInfo = util.getErpUserInfo();
    @SuppressWarnings ( "unused" )
    private UCUserInfo ucUserInfo = util.getUCUserInfo();
    @SuppressWarnings ( "unused" )
    private SessionInfo sessionInfo = util.getSessionInfo();


    /* App Builder Continue */
}'''

    junit = open('./'+fileData['menuCodeL']+'/service/impl/'+fileData['menuCodeU'] + 'ServiceTest.java', 'w',  encoding='UTF8')
    junit.write(content)
    junit.close()
