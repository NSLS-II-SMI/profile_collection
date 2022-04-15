# Running the test from IPython:
# %run -i ~/.ipython/profile_collection/acceptance_tests/run_all_tests.py


def test_pil1M():
    # it may be necessary to RE.clear_suspenders()
    sample_id(user_name="test", sample_name="test")
    det_exposure_time(0.5, 0.5)
    print("counting pil1M")
    uid, = RE(bp.count([pil1M]))
    print("accessing the count data")
    db[uid].table(fill=True)
    print("found the data")


test_pil1M()
