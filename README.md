# automation-ui-and-api
web和移动端ui、接口自动化框架集合

API：

    接口可以实现数据驱动，只维护Excel文档实现接口的自动化测试。
        Excel文档书写规范：
            每个sheet页是一个接口。每个sheet页下有一下列,列名严格区分大小写，用于区分请求数据请求的参数放在前几列，
            参照apiData/autotest-api.excel请求的参数如果想模拟某一个参数不传值时可以填写“null”。想模拟不传某一参数时可以不填。
            单元格中的数字xlrd读取后默认是保留小数点后面两位，因测试系统没有小数限制，读取的数字类型全部装换成了整数。
            apiData/autotest-api.excel中有示例。
            
            URL: 接口请求地址
            METHOD:请求方法
            RESULT：获取返回结果的命令
            EXPECT：预期结果
            RELY_API：当前接口所依赖的接口（sheet页名称）
            RELY_VALUE：当前接口所依赖的接口返回的数据获取方式。例如response_json["data"]-userId-account=laoji，以-分割。
            第一个元素是获取结果的语句，第二个元素是要获取的key，第三个元素是获取结果的条件（接口返回多条数据时大多使用列表的形式，
            此时需要遍历列表的数据，该条件是定位某一条数据的条件
            USERNAME：执行本接口需要的用户名
            PASSWORD：执行本接口需要的密码
            TYPE：测试用例的类型，forward为正向测试用例，接口作为依赖执行时只执行正向的测试用例，反向测试用例为空即可
            FILE：要上传的文件名加后缀，后台代码会自动拼接路径
            INITIALIZE：环境初始化sql语句，mysql-DELETE FROM sys_user WHERE account="laoji"，“-”以前的字符串用于区分数据库。
            RESTORE：环境还原要执行的sql语句
            
            