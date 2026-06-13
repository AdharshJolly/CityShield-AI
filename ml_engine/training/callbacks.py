def get_callbacks():
    """
    Returns a dictionary of Ultralytics YOLO callback hooks.
    """
    def on_train_epoch_end(trainer):
        # Example early stopping logic or custom LR stepping could go here.
        pass
        
    def on_fit_epoch_end(trainer):
        pass

    return {
        "on_train_epoch_end": on_train_epoch_end,
        "on_fit_epoch_end": on_fit_epoch_end
    }
