from django.shortcuts import render


def msoData(request):
    data_short = {
        "name": "this is my data",
        "wbs_data": {
            "wbs": ["S22-2001", "S22-2002", "S22-2003"],
            "cbu_po": "Dummy CBU PO",
            "financial_plan_status": "Done",
            "budgeted_amount": "$75,000",
            "billed_amount": '50,000',
            "unbilled_amount":'15,000'

        }
    }
    data_long = {
        "name": "this is my data",
        "wbs_data": [{
            "wbs": "S22-2001",
            "description": "Project Kick off",
            "milestone_due_date": "12/1/2022",
            "Cap_or_Exp": "Capital",
            "sow_mso_amount": '50,000',
            "haea_invoice":452319,
            "haea_invoice_date":"12/6/2022",
            "status":"Invoiced"

        },
        {
            "wbs": "S22-2001",
            "description": "Design Completion",
            "milestone_due_date": "1/15/2023",
            "Cap_or_Exp": "Capital",
            "sow_mso_amount": '50,000',
            "haea_invoice":'-',
            "haea_invoice_date":"-",
            "status":"Invoiced"

        },
        {
            "wbs": "S22-2001",
            "description": "Project Completion",
            "milestone_due_date": "2/15/2023",
            "Cap_or_Exp": "Capital",
            "sow_mso_amount": '25,000',
            "haea_invoice":'-',
            "haea_invoice_date":"-",
            "status":"Invoiced"

        },
        {
            "wbs": "S22-2001",
            "description": "Project Desc4",
            "milestone_due_date": "15/12/2022",
            "Cap_or_Exp": "Capital",
            "sow_mso_amount": '70,000',
            "haea_invoice":452319,
            "haea_invoice_date":"12/1/2022",
            "status":"Invoiced"

        },]
    }

    return render(request,'MSO/msoData.html',{'data_long'   :   data_long,
                                              'data_short'  :   data_short})



def msoDataUploadView(request):
    msoId = request.GET['msoId']
    if msoId == '1':
        msoData = ['MSO','Andy',1234,78956,'$50,000']
    elif msoId == '2':
        msoData = ['MSO','Tom',3456,78956,'$80,000']
    elif msoId == '3':
        msoData = ['MSO','Bob',67890,78956,'$10,0000']
    elif msoId == '4':
        msoData = ['MSO','Jenny',34564,78956,'$50,0000']
    else:
        msoData = None
    print(request.GET['msoId'],'msoidmsoidmsoidmsoid',msoData)
    return render(request, 'MSO/msoDataUploadView.html',{'msoData':msoData})