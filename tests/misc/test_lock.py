import pytest

from acondbs.misc.lock import TimeOutAcquiringLock, lock


def test_acquire_release(tmp_path_factory: pytest.TempPathFactory) -> None:
    folder = tmp_path_factory.mktemp('lock')
    lock_file = folder / '.lock'

    l = lock(lock_file)
    assert not l.locked
    l.acquire()
    assert l.locked
    assert lock_file.exists()
    l.release()
    assert not l.locked
    assert not lock_file.exists()


def test_release_when_not_locked(tmp_path_factory: pytest.TempPathFactory) -> None:
    folder = tmp_path_factory.mktemp('lock')
    lock_file = folder / '.lock'

    l = lock(lock_file)
    assert not l.locked
    l.release()
    assert not l.locked
    assert not lock_file.exists()


def test_release_not_delete_when_not_locked(
    tmp_path_factory: pytest.TempPathFactory,
) -> None:
    folder = tmp_path_factory.mktemp('lock')
    lock_file = folder / '.lock'

    lock_file.touch()

    l = lock(lock_file)
    assert not l.locked
    l.release()
    assert not l.locked
    assert lock_file.exists()


def test_acquire_timeout(tmp_path_factory: pytest.TempPathFactory) -> None:
    timeout = 0.1  # sec

    folder = tmp_path_factory.mktemp('lock')
    lock_file = folder / '.lock'

    lock_file.touch()

    l = lock(lock_file, timeout=timeout)

    with pytest.raises(TimeOutAcquiringLock):
        l.acquire()


def test_with_success(tmp_path_factory: pytest.TempPathFactory) -> None:
    folder = tmp_path_factory.mktemp('lock')
    lock_file = folder / '.lock'

    with lock(lock_file) as l:
        assert l.locked
        assert lock_file.exists()
    assert not l.locked
    assert not lock_file.exists()
