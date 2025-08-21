# VerSecBot - Smile Back

This plugin instructs VerSecBot to smile back at any messages containing a `:)`.

To use it, install the package and add the following block to your configuration:

```
[versecbot.plugins.smile_back]
    enabled = true

    [versecbot.plugins.smile_back.smile]
        enabled = true

        recognized_smiles = [":D"]
        smile_to_send = ":)"
```
