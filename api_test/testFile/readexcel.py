import xlrd

class ExcelUtil():
    def __init__(self,excelPath,sheetName='login'):
        self.data=xlrd.open_workbook(excelPath)
        self.table=self.data.sheet_by_name(sheetName)
        #获取第一行作为key值
        self.keys=self.table.row_values(0)

        self.rowNum=self.table.nrows#获取行数
        self.colNum=self.table.ncols#获取列数


    def dict_data(self):
        if self.rowNum<=1:
            print('总行数小于1')
        else:
            # print(self.rowNum)
            self.r=[]
            j=1
            for i in list(range(self.rowNum-1)):
                s={}
                s['rowNum']=i+2
                values=self.table.row_values(j)
                for x in list(range(self.colNum)):
                    s[self.keys[x]]=values[x]
                j = j + 1
                self.r.append(s)
            # print(self.r)
            return self.r


    # def get_data(path,sheet,caseName):
    #     self.r
    #     for i in datas:
    #         if datas[id]==caseName:
    #             return i




if __name__=='__main__':
    path='C://Users//Administrator//api_test//api_test//testFile//test cases.xlsx'
    execl_data=ExcelUtil(path)
    datas=execl_data.dict_data()
    # print(datas)
    # get_data(path=path,sheet='')
    for i in datas:
        if i['id']=='test_login_success':
            print(i)


