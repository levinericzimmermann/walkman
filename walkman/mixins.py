from __future__ import annotations

import functools

import pyo

import walkman

__all__ = (
    "PlayMixin",
    "JumpToMixin",
    "CloseMixin",
    "NamedMixin",
    "PyoObjectMixin",
    "DecibelMixin",
)


class PlayMixin(object):
    @property
    def is_playing(self) -> bool:
        try:
            return self._is_playing
        except AttributeError:
            return False

    def _play(self, duration: float = 0, delay: float = 0):
        ...

    def _stop(self, wait: float = 0):
        ...

    def play(self, duration: float = 0, delay: float = 0) -> PlayMixin:
        if not self.is_playing:
            self._play(duration=duration, delay=delay)
            self._is_playing = True
        return self

    def stop(self, wait: float = 0) -> PlayMixin:
        if self.is_playing:
            self._stop(wait=wait)
            self._is_playing = False
        return self


class JumpToMixin(object):
    def jump_to(self, time_in_seconds: float):
        ...


class CloseMixin(object):
    def close(self) -> CloseMixin:
        return self


class NamedMixin(object):
    @classmethod
    def get_class_name(cls) -> str:
        # class name
        return walkman.utilities.camel_case_to_snake_case(cls.__name__)

    def get_instance_name(self) -> str:
        try:
            return self._instance_name
        except AttributeError:
            self._instance_name = f"{self.get_class_name()}-{id(self)}"
            return self.get_instance_name()

    def __str__(self) -> str:
        return f"{type(self).__name__}({self.get_instance_name()})"

    def __hash__(self) -> int:
        return hash(self.get_instance_name())


class PyoObjectMixin(object):
    """Mixin for objects which consist of one or more pyo objects."""

    @functools.cached_property
    def pyo_object(self) -> pyo.PyoObject:
        return pyo.Sig(0)

    @property
    def pyo_object_or_float(self) -> pyo.PyoObject | float:
        return self.pyo_object

    @functools.cached_property
    def pyo_object_tuple(self) -> tuple[pyo.PyoObject, ...]:
        return (self.pyo_object,)

    @functools.cached_property
    def pyo_object_count(self) -> int:
        return len(self.pyo_object_tuple)


class DecibelMixin(object):
    @property
    def decibel(self) -> float:
        try:
            return self._decibel.getValue()
        except AttributeError:
            return -120

    @decibel.setter
    def decibel(self, value: float):
        try:
            self._decibel.setValue(value)
        except AttributeError:
            pass
