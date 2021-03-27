def common(fileData):
    content = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">

<mapper namespace="'''+fileData['path']+'''mapper.I'''+fileData['menuCodeU']+'''Mapper">
	<select id="getData"
		parameterType=""
		resultType="">
	</select>
</mapper>
'''

    common = open('./'+fileData['menuCodeL']+'/query/common/'+fileData['menuCodeU'] + 'Query.xml', 'w',  encoding='UTF8')
    common.write(content)
    common.close()
