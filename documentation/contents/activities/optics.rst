.. _ref_act_opt_serv:

Optical Spectroscopy Platform
=============================

In the *Optical platform* the Working Unit is half a day.
The *New Working Units* form for the Optical Spectroscopy Platform is shown on :numref:`fig_optics`. All fields
are mandatory and briefly explained below:

.. _fig_optics:

.. figure:: /images/optics.png
   :alt: optics

   Form to enter new Working Units


* *date* and *time* fields:  (see :numref:`fig_period`) specify a time interval from which the number of working
  units will be automatically calculated. The calculation excludes weekend days from the period.
* *Experiment*: this field lists all possible experiments within the platform. There are 3 particular cases related with
  the use of the chemistry spectrometers from room A125. For these, you have to enter manually the number of WUs you did
  in the given period. They can be set by step of 0.5.
* *Nnights*: number of nights during the time interval where a given experiment was running late (after 12PM). This adds
  one WU per late night.
* *WU*: number of working units during the interval
* *Project and PI*: select the project on which these WUs should be counted. If there is not a given funding project
  to use, then select the one called *Divers/Other Name*.
* *User*: the person doing the experiment. Automatically selected if the user is logged
* *Group*: its group, select it within the list. Automatically selected if the user is logged
* *Remark*: Some details on the ongoing experiment.

.. _fig_period:

.. figure:: /images/period.png
   :alt: optics

   Fields specifying a time interval

When you submit the form a summary will be displayed (see :numref:`fig_confirmation`). Please read it carefully before
clicking yes, as only the head of the given activity (here `Sébastien Weber`_) will be able to modify the record you just saved.




.. _fig_confirmation:

.. figure:: /images/confirmation.png
   :alt: optics

   Popup window displaying a summary of the record before it is processed.


.. _Sébastien Weber: sebastien.weber@cemes.fr