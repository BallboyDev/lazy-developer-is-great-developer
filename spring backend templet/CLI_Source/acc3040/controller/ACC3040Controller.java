package klago.financial.acc.acc3000.acc3040.controller;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import klago.financial.acc.acc3000.acc3040.service.IACC3040Service;
import klago.util.module.annotation.KlagoController;

/**
 * Name : ACC3040Controller
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
@Controller
@KlagoController
public class ACC3040Controller{
    
    @Autowired
    IACC3040Service service;

    /**
	 * 		value : "모듈약자(3자리, padStart(3, '0') 적용) + 기능(조회 : 00 / 생성 : 01 / 수정 : 02 / 삭제 : 03) + 순번(3자리)"
	 * 		인  사 : 0hr00001
	 * 		회  계 : 00a01001, 
	 *      개인화 : 0ap99001, 0hp01001
	 * 		예  제 : 0ex00001, 0ex01001, 0ex02001, 0ex99001
	 */
    
    /*
    @RequestMapping(value="/ACC3040/00a00001", method= {RequestMethod.POST})
	@ResponseBody
	public Object getData(HttpServletRequest servletRequest, HttpServletResponse servletResponse,
			@RequestBody P_ACC3040GetData param) throws Exception {
		return this.service.getData(param);
	}
    */

    /* App Builder Continue */
    
}