from urichat import register
from uri_control.edge.runtime import Runtime


def test_chat_uri_execute_dry_run():
    rt = Runtime(config={"chat": {"urisys_base_url": "http://127.0.0.1:8795"}})
    register(rt)
    res = rt.call(
        "chat://local/uri/command/execute",
        {"transcript": "kliknij OK", "dry_run": True, "approved": True},
        {"approved": True, "dry_run": True},
    )
    assert res["ok"]
    assert res["result"]["mode"] == "dry_run"
    assert "kvm://" in res["result"]["uri"]
