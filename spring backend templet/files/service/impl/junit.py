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

import '''+fileData['path']+'''service.I'''+fileData['menuCodeU']+'''Service;
import klago.'''+fileData['moduleName']+'''util.extend.ExtendsController;
import klago.'''+fileData['moduleName']+'''util.model.BaseContext;
import klago.'''+ ( "sample" if fileData['moduleName'] == "financial" else "humanutil" ) + '''.model.RequestModel;
import klago.util.model.APIResult;
import klago.util.model.ERPUserInfo;
import klago.util.model.SessionInfo;
import klago.util.model.UCUserInfo;

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

public class '''+fileData['menuCodeU']+'''ServiceTest extends ExtendsController{
    @SuppressWarnings ( "unused" )
    private Logger logger = LoggerFactory.getLogger('''+fileData['menuCodeU']+'''ServiceTest.class);
    @SuppressWarnings ( "unused" )
    private UCUserInfo  ucUserInfo  = new UCUserInfo();
    @SuppressWarnings ( "unused" )
    private ERPUserInfo erpUserInfo = new ERPUserInfo();
    private BaseContext baseContext = new BaseContext();
    private SessionInfo sessionInfo = new SessionInfo(); 

    @Autowired
    '''+fileData['menuCodeU']+'''Service service;

    @Before
    public void setUp ( ) {
        ucUserInfo.setGroupSeq("klagoDev");
        ucUserInfo.setLoginId("admin");
        ucUserInfo.setEmpSeq("1");
        ucUserInfo.setEmpName("관리자");
        ucUserInfo.setLangCode("kr");
        ucUserInfo.setUserSe("USER");
        ucUserInfo.setEmailAdd("admin");
        ucUserInfo.setEmailDomain("test.com");
        ucUserInfo.setEaType("eap");
        ucUserInfo.setPicFileId("");
        ucUserInfo.setClientIp("");
        ucUserInfo.setCompSeq("1000");
        ucUserInfo.setCompName("klagoDev");
        ucUserInfo.setBizSeq("1000");
        ucUserInfo.setBizName("기본사업장");
        ucUserInfo.setDeptSeq("1110");
        ucUserInfo.setDeptName("관리팀");
        ucUserInfo.setPositionCode("A8");
        ucUserInfo.setPositionName("사원");
        ucUserInfo.setDutyCode("A8");
        ucUserInfo.setDutyName("사원");
        ucUserInfo.setAuthorCode("A2");
        ucUserInfo.setErpCompSeq("3200");
        ucUserInfo.setErpBizSeq("");
        ucUserInfo.setErpDeptSeq("");
        ucUserInfo.setEmpSeq("06010001");
        ucUserInfo.setDeptPathNm("기본사업장|경영관리부|관리부|관리팀");
        ucUserInfo.setCompMailUrl("http:\\\\/\\\\/dev.klago.co.kr:80");
        
        erpUserInfo.setCompanyCode("3200");
        erpUserInfo.setCompanyName("더존상사");
        erpUserInfo.setnGisu(20);
        erpUserInfo.setfDate("20180101");
        erpUserInfo.settDate("20181231");
        erpUserInfo.setBizareaCode("1000");
        erpUserInfo.setBizareaName("강촌산업본사");
        erpUserInfo.setDeptCode("1100");
        erpUserInfo.setDeptName("재경부");
        erpUserInfo.setUserCode("06010001");
        erpUserInfo.setUserName("박성수");
        erpUserInfo.setsFormat02(1);
        erpUserInfo.setsFormat03(0);
        erpUserInfo.setsFormat04(2);
        erpUserInfo.setsFormat05(2);
        erpUserInfo.setsFormat06(0);
        erpUserInfo.setsFormat07(2);
        erpUserInfo.setsFormat08(2);
        erpUserInfo.setsFormat10(2);
        erpUserInfo.setLanguage("KOR");
        erpUserInfo.setFstLanguage("KOR");
        erpUserInfo.setSubLanguage("KOR");
        
        sessionInfo.setUcUserInfo(ucUserInfo);
        sessionInfo.setErpUserInfo(erpUserInfo);
        
        baseContext.setUserInfo(sessionInfo);
    }  

    /* App Builder Continue */
}'''

    junit = open('./'+fileData['menuCodeL']+'/service/impl/'+fileData['menuCodeU'] + 'ServiceTest.java', 'w',  encoding='UTF8')
    junit.write(content)
    junit.close()
