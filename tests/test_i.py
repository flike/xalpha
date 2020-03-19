import sys

sys.path.insert(0, "../")
import xalpha as xa
import pandas as pd

path3 = "demo3.csv"
ir = xa.irecord(path3)


def test_irecord():
    assert len(ir.filter("SH501018")) == 7


def test_itrade():
    t = xa.itrade("SH512880", ir)
    assert round(t.xirrrate("20200313"), 2) == 12.49
    assert t.dailyreport().iloc[0]["基金名称"] == "证券ETF"


def test_imul():
    c = xa.imul(status=ir)
    assert round(c.combsummary("20200309").iloc[0]["投资收益率"], 2) == -1.39
    c.v_positions()
