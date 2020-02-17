create table FinanceReport
(
	id varchar(32) not null,
	stock_name varchar(32) default '' not null comment '股票名称',
	indicator_name varchar(32) default '' not null comment '指标名称',
	indicator_data varchar(32) default '' null comment '指标数值',
	finance_type int null comment '该行数据所属的财务报表的类型',
	finance_name varchar(32) default '' null comment '该行数据所属的财报种类名'
)
comment '某公司财务报表';

create unique index FinanceReport_id_uindex
	on FinanceReport (id);

alter table FinanceReport
	add constraint FinanceReport_pk
		primary key (id);
