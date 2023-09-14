from odoo import models, fields


class TmsBatchModel(models.Model):
    _name = "tms.batch"
    _description = "TMS batch"
    _order = "create_date"
    # code = fields.Char(size=64, required=True)
    # sequence = fields.Integer(string="sequence", required=False, default=100)
    name = fields.Char(string="User Name", required=True)
    flight_id = fields.Char(string="Flight no.", size=100, required=False)
    flight_from = fields.Char(string="始发地", size=100, required=False)
    flight_to = fields.Char(string="目的地", size=100, required=False)
    flight_departure = fields.Datetime('起飞日期', default=lambda self: fields.Datetime.now())
    flight_landing = fields.Datetime('降落日期', default=lambda self: fields.Datetime.now())
    flight_route = fields.Char(string="航空路由", size=100, required=False)
    customs_proxy = fields.Char(string="清关代理", size=100, required=False)
    delivery_status = fields.Char(string="物流状态", size=100, required=False)
    delivery_address = fields.Char(string="派送地址", size=100, required=False)
    mawb = fields.Char(string="MAWB", size=100, required=False)
    hawb = fields.Char(string="HAWB", size=100, required=False)
    weight = fields.Float('重量', default=10)
    length = fields.Float('长', default=10)
    width = fields.Float('宽', default=10)
    height = fields.Float('高', default=10)
    pallet_num = fields.Integer('卡板数量', default=1)
    remark = fields.Char(string="备注", required=False)
    create_date = fields.Datetime('Create Time', default=lambda self: fields.Datetime.now())
    update_date = fields.Datetime('Update Time', default=lambda self: fields.Datetime.now())
