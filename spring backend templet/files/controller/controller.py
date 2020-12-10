def controller(fileData):
    content = '''package '''+fileData['path']+'''controller;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import '''+fileData['path']+'''service.I'''+fileData['menuCodeU']+'''Service;
import klago.util.module.annotation.KlagoController;

/**
 * Name : '''+fileData['menuCodeU']+'''Controller
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
@RequestMapping(value="/'''+fileData['menuCodeL']+'''")
public class '''+fileData['menuCodeU']+'''Controller{
    
    @Autowired
    I'''+fileData['menuCodeU']+'''Service service;
    
    /*
    @RequestMapping(value="/getData", method= {RequestMethod.POST})
	@ResponseBody
	public Object getData(HttpServletRequest servletRequest, HttpServletResponse servletResponse,
			@RequestBody P_''' + fileData['menuCodeU'] + '''GetData param) throws Exception {
		return this.service.getData(param);
	}
    */

    /* App Builder Continue */
    
}'''

    controller = open('./'+fileData['menuCodeL']+'/controller/'+fileData['menuCodeU'] + 'Controller.java', 'w',  encoding='UTF8')
    controller.write(content)
    controller.close()
