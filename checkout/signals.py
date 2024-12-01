from django.db.models.signals import post_save, post_delete

@reciever(post_save, sender= OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):

    instance.order.update_total()

@reciever(post_save, sender= OrderLineItem)
def update_on_delete(sender, instance, created, **kwargs):

    instance.order.update_total()