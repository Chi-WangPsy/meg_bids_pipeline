from mne_bids import BIDSPath, read_raw_bids

def load_raw_bids(bids_root, subject, session, task, run='01'):
    bids_path = BIDSPath(
        root=bids_root,
        subject=subject,
        session=session,
        task=task,
        run=run,
        datatype='meg',
        extension='.fif'
    )
    raw = read_raw_bids(bids_path=bids_path, verbose=False)
    return raw
