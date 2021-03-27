def iservice(fileData):
    content = '''package '''+fileData['path']+'''service;

import java.util.List;

/**
 * Name : I'''+fileData['menuCodeU']+'''Service
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
public interface I'''+fileData['menuCodeU']+'''Service {
    
    /* App Builder Continue */

}'''

    iservice = open('./'+fileData['menuCodeL']+'/service/I'+fileData['menuCodeU'] + 'Service.java', 'w',  encoding='UTF8')
    iservice.write(content)
    iservice.close()
