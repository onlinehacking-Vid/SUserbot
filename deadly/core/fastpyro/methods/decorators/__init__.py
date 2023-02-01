from deadly.core.fastpyro.methods.decorators.on_message import (
    OnMessage
) 

from deadly.core.fastpyro.methods.decorators.on_callback import (
    OnCallbackQuery
) 

from deadly.core.fastpyro.methods.decorators.on_inline import (
    OnInlineQuery
) 

class Decorators(
	OnMessage,
	OnInlineQuery,
	OnCallbackQuery,
):
	pass
